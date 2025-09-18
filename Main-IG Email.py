import asyncio
from nbconvert import NotebookExporter
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat import read, write

print("setting policy")
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

input_ntbk = "J:\\7A. IG-Main Email\\v11.ipynb"
output_ntbk = "J:\\7A. IG-Main Email\\v11.ipynb"

print("loading ntbk")

with open(input_ntbk, "r", encoding="utf-8") as f:
	notebook = read(f, as_version=4)

print("executing ntbk")
executor = ExecutePreprocessor(timeout=600, kernel_name="python3")
executor.preprocess(notebook, {'metadata': {'path': "J:\\7A. IG-Main Email\\"}})

print("saving ntbk")
with open(output_ntbk, "w", encoding="utf-8") as f:
	write(notebook,f)

print("Done")