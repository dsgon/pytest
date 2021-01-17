# Pytest intro
Codigo de ejemplo para la utilizacion de Pytest 

### Prerequisitos

> #### Python 
> - [Python](https://www.python.org/downloads/)
> - Descarga la ultima version estable o alguna >= a 3.8.0
> - Instala Python y configura su variable de entorno.
> - Podes verificar tu version de Python con el comando *python --version* en cualquier consola o terminal

### Instalacion

> #### Pytest y Pytest-HTML
> - Podes instalar los modulos de pytest y pytets-html desde el archivo *requirements.txt* utilizando *pip*
> ```
> pip install -r requirements.txt
> ```
> - Tambien podes hacerlo directo utilizando el comando *pip install pytest* y *pip install pytest-html*

### Configuracion
> Para agregar marks deben agregar los mismo en el archivo  **pytest.ini**.


## Ejecutando los Tests

> Para ejecutar los test se puede realizar desde cualquier consola o terminal, ubicados en la raiz del proyecto de las siguientes formas.

> #### Ejecucion Completa
> ```
> ~\pytest> python -m pytest .\test_pytest.py
> ```

> #### Ejecucion con reporte
> ```
> ~\pytest> python -m pytest .\test_pytest.py --html=.\report\pytest_report.html
> ```

> #### Ejecucion por marks y reporte
> ```
> ~\pytest> python -m pytest -m smoke .\test_pytest.py --html=.\report\pytest_report.html
> ```

## Reporte
> - Los reportes se generan en el path que se le indique al parametro *--html=*
> - A modo demoistrativo ente repositorio contiene una carpeta *report* donde se encuentra el reporte generado. 


## Documentacion
> - [Pytest](https://docs.pytest.org/en/stable/)
> - [Pytest-Html](https://github.com/pytest-dev/pytest-html)
> - [Pytest Marks](https://docs.pytest.org/en/reorganize-docs/new-docs/user/pytestmark.html)
> - [Pytest Working with custom marks](https://docs.pytest.org/en/stable/example/markers.html)

## Autor

* **David Gonzalez** - [github](https://github.com/dsgon/) - [twitter](https://twitter.com/__dsgon) - [linkedin](https://www.linkedin.com/in/dsgon/)

## Licencia

* **GNU GENERAL PUBLIC LICENSE**