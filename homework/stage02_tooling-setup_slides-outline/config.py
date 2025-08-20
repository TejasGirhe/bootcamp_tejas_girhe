{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7cb8288-3449-4b99-b412-94eff5011edd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from dotenv import load_dotenv\n",
    "import os\n",
    "\n",
    "# Load variables from .env\n",
    "load_dotenv()\n",
    "\n",
    "# Access them\n",
    "api_key = os.getenv(\"API_KEY\")\n",
    "data_dir = os.getenv(\"DATA_DIR\")\n",
    "\n",
    "print(\"API_KEY present:\", bool(api_key))\n",
    "print(\"DATA_DIR:\", data_dir)\n"
   ]
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
