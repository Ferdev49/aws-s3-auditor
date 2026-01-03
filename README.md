# AWS Cloud Governance: Automated S3 Security Auditor

## 🛡️ Propósito del Proyecto
En entornos empresariales, la exposición accidental de datos a través de S3 Buckets es uno de los riesgos más críticos (Misconfigurations). Esta herramienta de **Security-as-Code** automatiza la auditoría de buckets para asegurar el cumplimiento de las políticas de **Public Access Block**.

## 🚀 Capacidades Técnicas
* **Auditoría Multi-Recurso:** Escaneo recursivo de todos los buckets S3 mediante la API oficial `boto3`.
* **Generación de Evidencia (Audit Trail):** Creación automática de reportes en formato CSV con marcas de tiempo (timestamp) para trazabilidad.
* **Análisis de Riesgos:** Clasificación visual y documental de estados de seguridad (SEGURO vs. RIESGO).

## 🛠️ Stack Tecnológico
* **Python 3.13** (Manejo de entornos virtuales `.venv`).
* **AWS SDK (Boto3)** para integración con la nube.
* **IAM (Identity and Access Management):** Ejecución bajo el principio de menor privilegio.

## 📊 Ejemplo de Salida (Reporte de Cumplimiento)
El script genera un reporte estructurado para el equipo de Ciberseguridad:
| Nombre del Bucket | Estado de Seguridad | Acción Requerida |
| :--- | :--- | :--- |
| bucket-prueba-fer | SEGURO | Ninguna |
| datos-sensibles-temp | RIESGO: ACCESO PÚBLICO | Activar Public Access Block |

## ⚙️ Instalación y Uso
1. Clonar el repositorio.
2. Configurar credenciales de AWS: `aws configure`.
3. Instalar dependencias: `pip install -r requirements.txt`.
4. Ejecutar auditoría: `python S3_auditor.py`.
