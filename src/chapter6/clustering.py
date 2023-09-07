'''
Created on Sep 6, 2023

@author: immanueltrummer
'''
import argparse
import openai
import pandas as pd
import time

from sklearn.cluster import KMeans


def get_embedding(text):
    """ Calculate embedding vector for input text.
    
    Args:
        text: calculate embedding for this text.
    
    Returns:
        Vector representation of input text.
    """
    for nr_retries in range(1, 4):
        try:
            response = openai.Embedding.create(
                model='text-embedding-ada-002',
                input=text)
            return response['data'][0]['embedding']
        except:
            time.sleep(nr_retries * 2)
    raise Exception('Cannot query OpenAI model!')


def get_kmeans(embeddings, k):
    """ Cluster embedding vectors using K-means.
    
    Args:
        embeddings: embedding vectors.
        k: number of result clusters.
    
    Returns:
        cluster IDs in embedding order.
    """
    kmeans = KMeans(n_clusters=k, init='k-means++')
    kmeans.fit(embeddings)
    return kmeans.labels_


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Path to input file')
    parser.add_argument('nr_clusters', type=int, help='Number of clusters')
    parser.add_argument('openai_key', type=str, help='OpenAI access key')
    args = parser.parse_args()
    
    openai.api_key = args.openai_key
    df = pd.read_csv(args.file_path)
    
    embeddings = df['text'].apply(get_embedding)
    df['clusterid'] = get_kmeans(list(embeddings), args.nr_clusters)
    
    df.to_csv('result.csv')