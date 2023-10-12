{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f737941d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import io\n",
    "import pandas as pd\n",
    "import requests\n",
    "if 'data_loader' not in globals():\n",
    "    from mage_ai.data_preparation.decorators import data_loader\n",
    "if 'test' not in globals():\n",
    "    from mage_ai.data_preparation.decorators import test\n",
    "\n",
    "\n",
    "@data_loader\n",
    "def load_data_from_api(*args, **kwargs):\n",
    "    \"\"\"\n",
    "    Template for loading data from API\n",
    "    \"\"\"\n",
    "    url = 'https://storage.googleapis.com/uber-data-engineering-project-sss/data.csv'\n",
    "    response = requests.get(url)\n",
    "\n",
    "    return pd.read_csv(io.StringIO(response.text), sep=',')\n",
    "\n",
    "\n",
    "@test\n",
    "def test_output(output, *args) -> None:\n",
    "    \"\"\"\n",
    "    Template code for testing the output of the block.\n",
    "    \"\"\"\n",
    "    assert output is not None, 'The output is undefined'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a5b9731",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
