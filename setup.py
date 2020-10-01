from setuptools import setup, find_packages

setup(
    name='explainerdashboard',
    version='0.2.4',
    description='explainerdashboard allows you quickly build an interactive dashboard to explain the inner workings of your machine learning model.',
    long_description="""

This package makes it convenient to quickly deploy a dashboard web app
that explains the workings of a (scikit-learn compatible) fitted machine 
learning model. The dashboard provides interactive plots on model performance, 
feature importances, feature contributions to individual predictions, 
partial dependence plots, SHAP (interaction) values, visualisation of individual
decision trees, etc. 


The goal is manyfold:

    - Make it easy for data scientists to quickly inspect the inner workings and 
        performance of their model with just a few lines of code
    - Make it possible for non data scientist stakeholders such as managers, 
        directors, internal and external watchdogs to interactively inspect 
        the inner workings of the model without having to depend on a data 
        scientist to generate every plot and table
    - Make it easy to build a custom application that explains individual 
        predictions of your model for customers that ask for an explanation
    - Explain the inner workings of the model to the people working with 
        model in a human-in-the-loop deployment so that they gain understanding 
        what the model does and doesn't do. 
        This is important so that they can gain an intuition for when the 
        model is likely missing information and may have to be overruled.

The dashboard includes:

    - SHAP values (i.e. what is the contribution of each feature to each 
        individual prediction?)
    - Permutation importances (how much does the model metric deteriorate 
        when you shuffle a feature?)
    - Partial dependence plots (how does the model prediction change when 
        you vary a single feature?
    - Shap interaction values (decompose the shap value into a direct effect 
        an interaction effects)
    - For Random Forests and xgboost models: visualization of individual trees
        in the ensemble.  
    - Plus for classifiers: precision plots, confusion matrix, ROC AUC plot, 
        PR AUC plot, etc
    - For regression models: goodness-of-fit plots, residual plots, etc.

The library is designed to be modular so that it is easy to design your 
own custom dashboards so that you can focus on the layout and project specific 
textual explanations of the dashboard. (i.e. design it so that it will be 
interpretable for business users in your organization, not just data scientists)


A deployed example can be found at http://titanicexplainer.herokuapp.com
""",
    license='MIT',
    packages=find_packages(),
    package_dir={'explainerdashboard': 'explainerdashboard'},  # the one line where all the magic happens
    package_data={
        'explainerdashboard': ['assets/*', 'datasets/*'],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Dash",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"],
    install_requires=['dash', 'dash-bootstrap-components', 'jupyter_dash', 'dash-auth',
                    'dtreeviz>=1.0', 'numpy', 'pandas', 'PDPbox', 'scikit-learn', 
                    'shap', 'shortuuid'],
    author='Oege Dijk',
    author_email='oegedijk@gmail.com',
    keywords=['machine learning', 'explainability', 'shap', 'feature importances', 'dash'],
    url='https://github.com/oegedijk/explainerdashboard',
    project_urls={
        "Github page": "https://github.com/oegedijk/explainerdashboard/",
        "Documentation": "https://explainerdashboard.readthedocs.io/",
    },
)
