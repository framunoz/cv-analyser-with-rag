* [ ] (Opcional) hacer pipeline del notebook 01-fmg-rag
    * [ ] Investigar si se puede guardar un chromadb en memoria
    * [ ] (MUUUY OPCIONAL) Separar la parte de chromadb (salvado de embedding) y la parte de query en dos notebooks diferentes

* [ ] Hacer una rama para experimentar como pasar un curriculum de pdf en el json que tenemos (esto será otra pipeline)
    * [ ] Hacer curriculum ficticio (con chatgpt) y oferta ficticia
      * [ ] Investigar si se puede pasar un pdf directo al modelo (en un path o algo así)
        * [ ] Si no, investigar alguna librería pdf to text en python
    * [ ] Crear TypedDict del json resume (usar resume_example.json como ejemplo)
    * [ ] Hacer prompt para que el modelo genere el json resume a partir del pdf

* [ ] Traducir y documentar el notebook generado
