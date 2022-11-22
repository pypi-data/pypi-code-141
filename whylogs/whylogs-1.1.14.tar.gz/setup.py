# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['whylogs',
 'whylogs.api',
 'whylogs.api.fugue',
 'whylogs.api.logger',
 'whylogs.api.pyspark.experimental',
 'whylogs.api.reader',
 'whylogs.api.store',
 'whylogs.api.usage_stats',
 'whylogs.api.writer',
 'whylogs.core',
 'whylogs.core.constraints',
 'whylogs.core.constraints.factories',
 'whylogs.core.metrics',
 'whylogs.core.model_performance_metrics',
 'whylogs.core.proto',
 'whylogs.core.proto.v0',
 'whylogs.core.utils',
 'whylogs.core.validators',
 'whylogs.core.view',
 'whylogs.datasets',
 'whylogs.datasets.descr',
 'whylogs.extras',
 'whylogs.migration',
 'whylogs.viz',
 'whylogs.viz.enums',
 'whylogs.viz.extensions',
 'whylogs.viz.extensions.reports',
 'whylogs.viz.utils']

package_data = \
{'': ['*'],
 'whylogs.viz': ['html/*',
                 'html/css/*',
                 'html/fonts/*',
                 'html/images/*',
                 'html/js/*',
                 'html/templates/*']}

install_requires = \
['protobuf>=3.19.4', 'whylogs-sketching>=3.4.1.dev3']

extras_require = \
{':extra == "viz" or extra == "whylabs"': ['requests>=2.27,<3.0'],
 ':python_version < "3.11"': ['typing-extensions>=3.10'],
 ':python_version < "3.8"': ['importlib-metadata<4.3'],
 'datasets': ['pandas'],
 'docs': ['sphinx',
          'sphinx-autoapi',
          'sphinx-copybutton>=0.5.0,<0.6.0',
          'myst-parser[sphinx]>=0.17.2,<0.18.0',
          'furo>=2022.3.4,<2023.0.0',
          'sphinx-autobuild>=2021.3.14,<2022.0.0',
          'sphinxext-opengraph>=0.6.3,<0.7.0',
          'sphinx-inline-tabs',
          'ipython_genutils>=0.2.0,<0.3.0',
          'nbsphinx>=0.8.9,<0.9.0',
          'nbconvert>=7.0.0,<8.0.0'],
 'fugue': ['fugue>=0.7.3,<0.8.0'],
 'gcs': ['google-cloud-storage>=2.5.0,<3.0.0'],
 'image': ['Pillow>=9.2.0,<10.0.0'],
 'mlflow': ['mlflow-skinny>=1.26.1,<2.0.0'],
 's3': ['boto3>=1.22.13,<2.0.0'],
 'spark': ['pyarrow>=8.0.0,<9.0.0', 'pyspark>=3.0.0,<4.0.0'],
 'viz': ['pybars3>=0.9,<0.10',
         'ipython',
         'numpy',
         'whylabs-client==0.4.0',
         'Pillow>=9.2.0,<10.0.0'],
 'viz:python_version < "3.11"': ['scipy>=1.5'],
 'whylabs': ['whylabs-client==0.4.0']}

setup_kwargs = {
    'name': 'whylogs',
    'version': '1.1.14',
    'description': 'Profile and monitor your ML data pipeline end-to-end',
    'long_description': '<img src="https://static.scarf.sh/a.png?x-pxid=bc3c57b0-9a65-49fe-b8ea-f711c4d35b82" /><p align="center">\n<img src="https://i.imgur.com/nv33goV.png" width="35%"/>\n</br>\n\n<h1 align="center">The open standard for data logging\n\n </h1>\n  <h3 align="center">\n   <a href="https://whylogs.readthedocs.io/"><b>Documentation</b></a> &bull;\n   <a href="https://bit.ly/whylogsslack"><b>Slack Community</b></a> &bull;\n   <a href="https://github.com/whylabs/whylogs#python-quickstart"><b>Python Quickstart</b></a> &bull;\n   <a href="https://whylogs.readthedocs.io/en/latest/examples/integrations/writers/Writing_to_WhyLabs.html"><b>WhyLabs Quickstart</b></a>\n </h3>\n\n<p align="center">\n<a href="https://github.com/whylabs/whylogs-python/blob/mainline/LICENSE" target="_blank">\n    <img src="http://img.shields.io/:license-Apache%202-blue.svg" alt="License">\n</a>\n<a href="https://badge.fury.io/py/whylogs" target="_blank">\n    <img src="https://badge.fury.io/py/whylogs.svg" alt="PyPi Version">\n</a>\n<a href="https://github.com/python/black" target="_blank">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">\n</a>\n<a href="https://pepy.tech/project/whylogs" target="_blank">\n    <img src="https://pepy.tech/badge/whylogs" alt="PyPi Downloads">\n</a>\n<a href="bit.ly/whylogs" target="_blank">\n    <img src="https://github.com/whylabs/whylogs-python/workflows/whylogs%20CI/badge.svg" alt="CI">\n</a>\n<a href="https://codeclimate.com/github/whylabs/whylogs-python/maintainability" target="_blank">\n    <img src="https://api.codeclimate.com/v1/badges/442f6ca3dca1e583a488/maintainability" alt="Maintainability">\n</a>\n</p>\n\n## What is whylogs\n\nwhylogs is an open source library for logging any kind of data. With whylogs, users are able to generate summaries of their datasets (called _whylogs profiles_) which they can use to:\n\n1. Track changes in their dataset\n2. Create _data constraints_ to know whether their data looks the way it should\n3. Quickly visualize key summary statistics about their datasets\n\nThese three functionalities enable a variety of use cases for data scientists, machine learning engineers, and data engineers:\n\n- Detect data drift in model input features\n- Detect training-serving skew, concept drift, and model performance degradation\n- Validate data quality in model inputs or in a data pipeline\n- Perform exploratory data analysis of massive datasets\n- Track data distributions & data quality for ML experiments\n- Enable data auditing and governance across the organization\n- Standardize data documentation practices across the organization\n- And more\n\n<a href="https://hub.whylabsapp.com/signup" target="_blank">\n    <img src="https://user-images.githubusercontent.com/7946482/193939278-66a36574-2f2c-482a-9811-ad4479f0aafe.png" alt="WhyLabs Signup">\n</a>\n\nIf you have any questions, comments, or just want to hang out with us, please join [our Slack Community](https://bit.ly/rsqrd-slack). In addition to joining the Slack Community, you can also help this project by giving us a ⭐ in the upper right corner of this page.\n\n## Python Quickstart<a name="python-quickstart" />\n\nInstalling whylogs using the pip package manager is as easy as running `pip install whylogs` in your terminal.\n\nFrom here, you can quickly log a dataset:\n\n```python\nimport whylogs as why\nimport pandas as pd\n\n#dataframe\ndf = pd.read_csv("path/to/file.csv")\nresults = why.log(df)\n```\n\nAnd voilà, you now have a whylogs profile. To learn more about about a whylogs profile is and what you can do with it, read on.\n\n## Table of Contents\n\n- [whylogs Profiles](#whylogs-profiles)\n- [Data Constraints](#data-constraints)\n- [Profile Visualization](#profile-visualization)\n- [Integrations](#integrations)\n- [Supported Data Types](#data-types)\n- [Examples](#examples)\n- [Usage Statistics](#usage-statistics)\n- [Community](#community)\n- [Contribute](#contribute)\n\n## whylogs Profiles<a name="whylogs-profiles" />\n\n### What are profiles\n\nwhylogs profiles are the core of the whylogs library. They capture key statistical properties of data, such as the distribution (far beyond simple mean, median, and standard deviation measures), the number of missing values, and a wide range of configurable custom metrics. By capturing these summary statistics, we are able to accurately represent the data and enable all of the use cases described in the introduction.\n\nwhylogs profiles have three properties that make them ideal for data logging: they are **efficient**, **customizable**, and **mergeable**.\n\n<br />\n\n<img align="left" src="https://user-images.githubusercontent.com/7946482/171064257-26bf727e-3480-4ec3-9c9d-5d8a79567bca.png">\n\n**Efficient**: whylogs profiles efficiently describe the dataset that they represent. This high fidelity representation of datasets is what enables whylogs profiles to be effective snapshots of the data. They are better at capturing the characteristics of a dataset than a sample would be—as discussed in our [Data Logging: Sampling versus Profiling](https://whylabs.ai/blog/posts/data-logging-sampling-versus-profiling) blog post—and are very compact.\n\n<br />\n\n<img align="left" src="https://user-images.githubusercontent.com/7946482/171064575-72ee0f76-7365-4fd1-9cab-4debb673baa8.png">\n\n**Customizable**: The statistics that whylogs profiles collect are easily configured and customizable. This is useful because different data types and use cases require different metrics, and whylogs users need to be able to easily define custom trackers for those metrics. It’s the customizability of whylogs that enables our text, image, and other complex data trackers.\n\n<br />\n\n<img align="left" src="https://user-images.githubusercontent.com/7946482/171064525-2d314534-6cdb-4c07-9d9f-5c74d5c03029.png">\n\n**Mergeable**: One of the most powerful features of whylogs profiles is their mergeability. Mergeability means that whylogs profiles can be combined together to form new profiles which represent the aggregate of their constituent profiles. This enables logging for distributed and streaming systems, and allows users to view aggregated data across any time granularity.\n\n<br />\n\n### How do you generate profiles\n\nOnce whylogs is installed, it\'s easy to generate profiles in both Python and Java environments.\n\nTo generate a profile from a Pandas dataframe in Python, simply run:\n\n```python\nimport whylogs as why\nimport pandas as pd\n\n#dataframe\ndf = pd.read_csv("path/to/file.csv")\nresults = why.log(df)\n```\n\n<!---\nFor images, replace `df` with `image="path/to/image.png"`. Similarly, you can profile Python dicts by replacing the dataframe within the `log()` function with a Python `dict` object.\n--->\n\n### What can you do with profiles\n\nOnce you’ve generated whylogs profiles, a few things can be done with them:\n\nIn your local Python environment, you can set data constraints or visualize your profiles. Setting data constraints on your profiles allows you to get notified when your data don’t match your expectations, allowing you to do data unit testing and some baseline data monitoring. With the Profile Visualizer, you can visually explore your data, allowing you to understand it and ensure that your ML models are ready for production.\n\nIn addition, you can send whylogs profiles to the SaaS ML monitoring and AI observability platform [WhyLabs](https://whylabs.ai). With WhyLabs, you can automatically set up monitoring for your machine learning models, getting notified on both data quality and data change issues (such as data drift). If you’re interested in trying out WhyLabs, check out the always free [Starter edition](https://whylabs.ai/free), which allows you to experience the entire platform’s capabilities with no credit card required.\n\n## WhyLabs<a name="whylabs" />\n\nWhyLabs is a managed service offering built for helping users make the most of their whylogs profiles. With WhyLabs, users can ingest profiles and set up automated monitoring as well as gain full observability into their data and ML systems. With WhyLabs, users can ensure the reliability of their data and models, and debug any problems that arise with them.\n\nIngesting whylogs profiles into WhyLabs is easy. After obtaining your access credentials from the platform, you’ll need to set them in your Python environment, log a dataset, and write it to WhyLabs, like so:\n\n```python\nimport whylogs as why\nimport os\n\nos.environ["WHYLABS_DEFAULT_ORG_ID"] = "org-0" # ORG-ID is case-sensitive\nos.environ["WHYLABS_API_KEY"] = "YOUR-API-KEY"\nos.environ["WHYLABS_DEFAULT_DATASET_ID"] = "model-0" # The selected model project "MODEL-NAME" is "model-0"\n\nresults = why.log(df)\n\nresults.writer("whylabs").write()\n```\n\n![image](<https://github.com/whylabs/whylogs/blob/assets/images/chrome-capture-2022-9-4%20(1).gif>)\n\nIf you’re interested in trying out WhyLabs, check out the always free [Starter edition](https://hub.whylabsapp.com/signup), which allows you to experience the entire platform’s capabilities with no credit card required.\n\n## Data Constraints<a name="data-constraints" />\n\nConstraints are a powerful feature built on top of whylogs profiles that enable you to quickly and easily validate that your data looks the way that it should. There are numerous types of constraints that you can set on your data (that numerical data will always fall within a certain range, that text data will always be in a JSON format, etc) and, if your dataset fails to satisfy a constraint, you can fail your unit tests or your CI/CD pipeline.\n\nA simple example of setting and testing a constraint is:\n\n```python\nimport whylogs as why\nfrom whylogs.core.constraints import Constraints, ConstraintsBuilder\nfrom whylogs.core.constraints.factories import greater_than_number\n\nprofile_view = why.log(df).view()\nbuilder = ConstraintsBuilder(profile_view)\nbuilder.add_constraint(greater_than_number(column_name="col_name", number=0.15))\n\nconstraints = builder.build()\nconstraints.report()\n```\n\nTo learn more about constraints, check out: the [Constraints Example](https://bit.ly/whylogsconstraintsexample).\n\n## Profile Visualization<a name="profile-visualization" />\n\nIn addition to being able to automatically get notified about potential issues in data, it’s also useful to be able to inspect your data manually. With the profile visualizer, you can generate interactive reports about your profiles (either a single profile or comparing profiles against each other) directly in your Jupyter notebook environment. This enables exploratory data analysis, data drift detection, and data observability.\n\nTo access the profile visualizer, install the `[viz]` module of whylogs by running `pip install "whylogs[viz]"` in your terminal. One type of profile visualization that we can create is a drift report; here\'s a simple example of how to analyze the drift between two profiles:\n\n```python\nimport whylogs as why\n\nfrom whylogs.viz import NotebookProfileVisualizer\n\nresult = why.log(pandas=df_target)\nprof_view = result.view()\n\nresult_ref = why.log(pandas=df_reference)\nprof_view_ref = result_ref.view()\n\nvisualization = NotebookProfileVisualizer()\nvisualization.set_profiles(target_profile_view=prof_view, reference_profile_view=prof_view_ref)\n\nvisualization.summary_drift_report()\n```\n\n![image](https://user-images.githubusercontent.com/7946482/169669536-a25cce95-acde-4637-b7b9-c2a685f0bc3f.png)\n\nTo learn more about visualizing your profiles, check out: the [Visualizer Example](https://bit.ly/whylogsvisualizerexample)\n\n## Data Types<a name="data-types" />\n\nwhylogs supports both structured and unstructured data, specifically:\n\n| Data type        | Features | Notebook Example                                                                                                                                                |\n| ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| Tabular Data     | ✅       | [Getting started with structured data](https://github.com/whylabs/whylogs/blob/mainline/python/examples/basic/Getting_Started.ipynb)                            |\n| Image Data       | ✅       | [Getting started with images](https://github.com/whylabs/whylogs/blob/maintenance/0.7.x/examples/logging_images.ipynb)                                          |\n| Text Data        | ✅       | [String Features](https://github.com/whylabs/whylogs/blob/maintenance/0.7.x/examples/String_Features.ipynb)                                                     |\n| Embeddings       | 🛠        |                                                                                                                                                                 |\n| Other Data Types | ✋       | Do you have a request for a data type that you don’t see listed here? Raise an issue or join our Slack community and make a request! We’re always happy to help |\n\n## Integrations\n\n![current integration](https://user-images.githubusercontent.com/7946482/171062942-01c420f2-7768-4b7c-88b5-e3f291e1b7d8.png)\n\nwhylogs can seamslessly interact with different tooling along your Data and ML pipelines. We have currently built integrations with:\n\n- AWS S3\n- Apache Airflow\n- Apache Spark\n- Mlflow\n- GCS\n\nand much more!\n\nIf you want to check out our complete list, please refer to our [integrations examples](https://github.com/whylabs/whylogs/tree/mainline/python/examples/integrations) page.\n\n## Examples\n\nFor a full set of our examples, please check out the [examples folder](https://github.com/whylabs/whylogs/tree/mainline/python/examples).\n\n## Usage Statistics<a name="whylogs-profiles" />\n\nStarting with whylogs v1.0.0, whylogs by default collects anonymous information about a user’s environment. These usage statistics do not include any information about the user or the data that they are profiling, only the environment that the user in which the user is running whylogs.\n\nTo read more about what usage statistics whylogs collects, check out the relevant [documentation](https://docs.whylabs.ai/docs/usage-statistics/).\n\nTo turn off Usage Statistics, simply set the `WHYLOGS_NO_ANALYTICS` environment variable to True, like so:\n\n```python\nimport os\nos.environ[\'WHYLOGS_NO_ANALYTICS\']=\'True\'\n```\n\n## Community\n\nIf you have any questions, comments, or just want to hang out with us, please join [our Slack channel](http://join.slack.whylabs.ai/).\n\n## Contribute\n\n### How to Contribute\n\nWe welcome contributions to whylogs. Please see our [contribution guide](https://github.com/whylabs/whylogs/blob/mainline/.github/CONTRIBUTING.md) and our [development guide](https://github.com/whylabs/whylogs/blob/mainline/.github/DEVELOPMENT.md) for details.\n\n### Contributors\n\n<a href="https://github.com/whylabs/whylogs/graphs/contributors">\n  <img src="https://contrib.rocks/image?repo=whylabs/whylogs" />\n</a>\n\nMade with [contrib.rocks](https://contrib.rocks).\n',
    'author': 'WhyLabs.ai',
    'author_email': 'support@whylabs.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://docs.whylabs.ai',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4',
}


setup(**setup_kwargs)
