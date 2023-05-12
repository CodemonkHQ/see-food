# SeeFood

SeeFood is a hotdog identifying app which utilises Machine Learning to identify whether a given image is hotdog or not. The app concept is heavily inspired by HBO's Silicon Valley series wherein the character Jìan-Yáng develops a similar mobile app for his startup.

SeeFood as a project was developed to explore and showcase the potential of [Flet](https://flet.dev) framework. This project is an accompaniment to the blog '**[Flet: Power of your favourite language + Flutter UI](https://codemonk.in/blog/flet-power-of-your-favorite-language-flutter-ui/)**'.


# Getting started

## Dependencies
SeeFood requires Python 3.7 or above.


## Installation instructions

To use the application, follow these steps:

1. Clone the repository on your machine.
2. Open a terminal and navigate to the project directory:

   ```sh
   cd /path/to/see-food-project
   ```

3. Create a new virtual environment by running the following command:

   ```sh
   python -m venv venv
   ```

   This will create a new virtual environment named "venv" in the project directory.

4. Activate the virtual environment by running the following command:

   On Windows:
   ```sh
   venv\Scripts\activate.bat
   ```

   On Unix or Linux:
   ```sh
   source venv/bin/activate
   ```

   You should see the name of the virtual environment in your terminal prompt.

5. Install the required packages using pip:

   ```sh
   pip install -r requirements.txt
   ```

   This will install the required packages in the virtual environment.

6. Run the application by running the following command:

   ```sh
   python main.py
   ```


## Usage

Upload any hotdog image or any random image by clicking the 'Upload File' button on the UI and see the magic yourself.

<img src="https://raw.githubusercontent.com/CodemonkHQ/see-food/80da92d81c7dd25c74e14527d95a7f5b00cce729/assets/extras/preview.gif" alt="Screenshot 4" width="600"/> 


## Project Structure

The project has a simple directory structure:

```
see-food/
  |-- main.py
  |-- label_dog.py
  |-- requirements.txt
  |-- LICENSE
  |-- README.md
```

- `main.py`: This is the entry point for the application.
- `label_dog.py`: This module contains the function to identify whether an image contains a hotdog or not. It uses a TensorFlow trained model for image recognition.
- `requirements.txt`: This file contains a list of Python packages required to run the application.
- `LICENSE`: This file contains the license for the project.
- `README.md`: This file contains information about the project.

## Project Attribution

The 'label_dog' TensorFlow model used in this project was originally developed by VPanjeta. You can find the original project [here](https://github.com/VPanjeta/hotdog-or-not-hotdog).

The 'label_dog' model is released under the license specified in VPanjeta's repository. Please refer to the original project for detailed license information.

Modifications:
- No modifications have been made to the 'label_dog' TensorFlow model. It is used as-is in this project.

Acknowledgments:
- We would like to express our gratitude to VPanjeta for developing the 'label_dog' model and making it available for public use.


## Contributor Guidelines
### Git
* See-food follows the [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow for development. All the development happens in the 'develop' branch.
* For commits, generally follow the [Udacity Git Commit Message Style Guide](https://udacity.github.io/git-styleguide/).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.