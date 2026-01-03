import boto3
import csv
from datetime import datetime

def auditar_s3():
    # 1. Conexión con el cliente de S3
    s3 = boto3.client('s3')
    respuesta = s3.list_buckets()
    
    # 2. Configuración de fecha y nombre de reporte
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    nombre_reporte = f"reporte_seguridad_s3_{fecha_hoy}.csv"
    
    # Corregido: ahora tiene la 'f' para que la fecha se vea bien
    print(f"--- INICIANDO AUDITORÍA: {fecha_hoy} ---")

    # 3. Creación del reporte CSV
    with open(nombre_reporte, mode='w', newline='', encoding='utf-8') as archivo_csv:
        campos = ['Nombre del Bucket', 'Estado de Seguridad', 'Accion Requerida']
        escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor.writeheader()

        for bucket in respuesta['Buckets']:
            nombre_bucket = bucket['Name']
            
            try:
                # Verificamos si tiene bloqueo de acceso público
                s3.get_public_access_block(Bucket=nombre_bucket)
                estado = "SEGURO"
                accion = "Ninguna"
                print(f"✅ {nombre_bucket}: Protegido")
                
            except:
                # Si falla la consulta, es que no tiene las restricciones activas
                estado = "RIESGO: ACCESO PÚBLICO"
                accion = "Activar Public Access Block de inmediato"
                print(f"❌ {nombre_bucket}: ¡ALERTA DE SEGURIDAD!")

            escritor.writerow({
                'Nombre del Bucket': nombre_bucket,
                'Estado de Seguridad': estado,
                'Accion Requerida': accion
            })

    print(f"\n--- AUDITORÍA FINALIZADA ---")
    print(f"📄 Reporte generado: {nombre_reporte}")

if __name__ == "__main__":
    auditar_s3()