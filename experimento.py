import pickle

with open("experimento_func_2_7_40.pkl", "rb") as f:
    data = pickle.loads(f.read())["func_2"]

with open("experimento_func_2_9_40.pkl", "rb") as f:
    data.extend(pickle.loads(f.read())["func_2"])

with open("experimento_func_2_12_40.pkl", "rb") as f:
    data.extend(pickle.loads(f.read())["func_2"])

with open("experimento_func_2_15_40.pkl", "rb") as f:
    data.extend(pickle.loads(f.read())["func_2"])

with open("experimento_func_2_18_40.pkl", "rb") as f:
    data.extend(pickle.loads(f.read())["func_2"])

with open("experimento_func_2.pkl", "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)