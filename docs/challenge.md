### DOCUMENTATION

- Model: Although both models showed almost the same results, I chose the XGBoost model because it can handle non-linear relationships, it has more hyperparameters. I felt that it was a model of more computational expense but my intention was also to know how it behaved.

-The project is deployed on Cloud Run, in cd.yml there is an example of how to implement the solution in aws ECS

- The application is deployed in a container through the Dockerfile
- The ci.yml file is used to execute the tests and if everything is correct, the cd.yml file is executed, which is in charge of deploying and updating the changes in the cloud.

- NOTE: I make this commit to mention that in the DEVELOP branch I finished the part of the stress test that was the only one that was pending. I don't merge here to master because the time limit has passed.
