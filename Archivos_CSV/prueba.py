# import csv
# def leer_csv(ruta: str) -> list[dict[str, str]]:
#     """Lee el archivo CSV y devuelve los datos como lista de diccionarios"""
#     try:
#         with open(ruta, 'r', encoding='utf-8') as archivo:
#             lector = csv.DictReader(archivo)
#             return list(lector)
#     except FileNotFoundError:
#         print(f"❌ Error: No se encontró el archivo {ruta}")
#         return []
    

# print(leer_csv('Archivos_CSV/canciones.csv'))

# def mostrar_lista_temas(canciones: list):
#     """Muestra la lista de temas en formato tabular"""
#     print("\n🎵 LISTA DE TEMAS - LADY GAGA")
#     print("=" * 60)
#     print(f"{'CÓDIGO':<10} {'TÍTULO':<30} {'DURACIÓN':<10}")
#     print("-" * 60)
    
#     for cancion in canciones:
#         duracion_formateada = f"{cancion.duracion//60}:{cancion.duracion%60:02d}"
#         print(f"{cancion.codigo:<10} {cancion.titulo[:28]:<30} {duracion_formateada:<10}")
    
#     print(f"\n📊 Total de canciones: {len(canciones)}")


