'''
Created on Sep 5, 2023

@author: immanueltrummer
'''
{
  "data": [
    {
      "created": 1607632725,
      "id": "curie:2020-05-03",
      "object": "model",
      "owned_by": "system",
      "parent": null,
      "permission": [
        {
          "allow_create_engine": false,
          "allow_fine_tuning": false,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1607632727,
          "group": null,
          "id": "snapperm-...",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "*"
        }
      ],
      "root": "curie:2020-05-03"
    },
    {
      "created": 1641833573,
      "id": "curie:ft-personal-2022-01-10-16-52-53",
      "object": "model",
      "owned_by": "user-...",
      "parent": "curie:2020-05-03",
      "permission": [
        {
          "allow_create_engine": true,
          "allow_fine_tuning": true,
          "allow_logprobs": true,
          "allow_sampling": true,
          "allow_search_indices": false,
          "allow_view": true,
          "created": 1641833573,
          "group": null,
          "id": "snapperm-...",
          "is_blocking": false,
          "object": "model_permission",
          "organization": "org-..."
        }
      ],
      "root": "curie:2020-05-03"
    },
    ...
}