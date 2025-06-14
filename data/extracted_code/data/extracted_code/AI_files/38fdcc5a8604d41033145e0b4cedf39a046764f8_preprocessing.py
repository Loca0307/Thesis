{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import spacy\n",
    "import os\n",
    "import pandas as pd\n",
    "\n",
    "from src.preprocessing import convert_txt_to_json, convert_to_conllu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████| 200/200 [00:01<00:00, 117.78it/s]\n"
     ]
    }
   ],
   "source": [
    "# convert txt file to JSON file\n",
    "input_file = \"../data/chatgpt_dataset.txt\"\n",
    "output_file = \"../data/chatgpt_dataset.json\"\n",
    "convert_txt_to_json(\n",
    "    input_file=input_file, output_file=output_file, link=\"https://chatgpt.com/\"\n",
    ")\n",
    "\n",
    "# convert JSON file to conllu dataset\n",
    "output_file = os.path.join(\"../data\", \"chatgpt_dataset.conllu\")\n",
    "nlp = spacy.load(\"en_core_web_sm\")\n",
    "file_path = \"../data/chatgpt_dataset.json\"\n",
    "data = pd.read_json(file_path, lines=True)\n",
    "convert_to_conllu(data, output_file, nlp)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}