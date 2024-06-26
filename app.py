import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

st.title("Molecule Visualization App")

# 사용자로부터 분자 구조 입력 받기
smiles = st.text_input("Enter a SMILES string:")

if smiles:
    # SMILES 문자열을 분자로 변환
    mol = Chem.MolFromSmiles(smiles)
    
    if mol:
        # 분자를 이미지로 변환
        img = Draw.MolToImage(mol)
        
        # 이미지 출력
        st.image(img)
    else:
        st.error("Invalid SMILES string!")
