from django.core.management.base import BaseCommand

from apps.threats.models import Threat
from apps.events.models import Event


class Command(BaseCommand):
    help = "Carga datos iniciales del proyecto"

    def handle(self, *args, **kwargs):

        threats_data = [
            {
                "name": "Phishing",
                "description": "Suplantación de identidad mediante correos, mensajes o sitios fraudulentos.",
                "owasp_category": "A07 - Identification and Authentication Failures",
                "recommendation": "Implementar MFA y verificar la legitimidad de los enlaces.",
                "risk_level": "HIGH",
            },
            {
                "name": "Sitio Web Clonado",
                "description": "Réplica de sitios legítimos para capturar credenciales y datos financieros.",
                "owasp_category": "A01 - Broken Access Control",
                "recommendation": "Verificar URL y certificados digitales.",
                "risk_level": "CRITICAL",
            },
            {
                "name": "Ingeniería Social",
                "description": "Manipulación psicológica para obtener información sensible de los usuarios.",
                "owasp_category": "A07 - Identification and Authentication Failures",
                "recommendation": "Capacitar usuarios y verificar siempre la identidad del solicitante.",
                "risk_level": "HIGH",
            },
            {
                "name": "Credential Stuffing",
                "description": "Uso de credenciales filtradas previamente para acceder a cuentas de usuarios.",
                "owasp_category": "A07 - Identification and Authentication Failures",
                "recommendation": "Implementar autenticación multifactor y contraseñas únicas.",
                "risk_level": "HIGH",
            },
            {
                "name": "Malware Promocional",
                "description": "Distribución de software malicioso mediante promociones o descargas falsas.",
                "owasp_category": "A08 - Software and Data Integrity Failures",
                "recommendation": "Descargar únicamente desde fuentes oficiales y mantener antivirus actualizado.",
                "risk_level": "HIGH",
            },
            {
                "name": "Smishing",
                "description": "Ataque de phishing realizado mediante mensajes SMS o mensajería móvil.",
                "owasp_category": "A07 - Identification and Authentication Failures",
                "recommendation": "No acceder a enlaces recibidos desde remitentes desconocidos.",
                "risk_level": "HIGH",
            },
            {
                "name": "Malvertising",
                "description": "Uso de anuncios publicitarios maliciosos para distribuir malware o redirigir a sitios fraudulentos.",
                "owasp_category": "A05 - Security Misconfiguration",
                "recommendation": "Verificar el destino de enlaces publicitarios y utilizar bloqueadores de contenido malicioso.",
                "risk_level": "MEDIUM",
            },
            {
                "name": "Robo de Sesión (Session Hijacking)",
                "description": "Obtención o reutilización de sesiones autenticadas para acceder a cuentas sin autorización.",
                "owasp_category": "A07 - Identification and Authentication Failures",
                "recommendation": "Utilizar HTTPS, MFA y expiración de sesiones.",
                "risk_level": "CRITICAL",
            },
            {
                "name": "Ataque Man-in-the-Middle (MITM)",
                "description": "Intercepción de comunicaciones para capturar información o credenciales.",
                "owasp_category": "A02 - Cryptographic Failures",
                "recommendation": "Utilizar conexiones seguras HTTPS y evitar redes no confiables.",
                "risk_level": "HIGH",
            },
            {
                "name": "Robo de Cookies de Sesión",
                "description": "Captura de cookies de autenticación para obtener acceso a cuentas de usuario.",
                "owasp_category": "A07 - Identification and Authentication Failures",
                "recommendation": "Utilizar cookies seguras, MFA y controles de expiración de sesión.",
                "risk_level": "CRITICAL",
            },
        ]

        for threat_data in threats_data:
            Threat.objects.get_or_create(
                name=threat_data["name"],
                defaults=threat_data
            )

        events_data = [
            {
                "name": "Cyberday",
                "event_date": "2026-07-31",
                "description": "Evento masivo de comercio electrónico con alta exposición a amenazas cibernéticas.",
                "risk_level": "CRITICAL",
            },
            {
                "name": "Black Friday",
                "event_date": "2026-11-27",
                "description": "Jornada internacional de descuentos con incremento de fraude y phishing.",
                "risk_level": "HIGH",
            },
            {
                "name": "Navidad",
                "event_date": "2026-12-26",
                "description": "Periodo comercial con aumento de compras online y campañas fraudulentas.",
                "risk_level": "MEDIUM",
            },
            {
                "name": "Fiestas Patrias",
                "event_date": "2026-09-18",
                "description": "Celebración nacional caracterizada por un aumento en compras online, reservas, promociones y transacciones digitales, incrementando la exposición a fraudes y suplantación de identidad.",
                "risk_level": "HIGH",
            },
            {
                "name": "Día de la Madre",
                "event_date": "2026-05-09",
                "description": "Fecha comercial de alta actividad en comercio electrónico y campañas promocionales, donde aumentan los intentos de phishing y sitios fraudulentos.",
                "risk_level": "MEDIUM",
            },
            {
                "name": "Regreso a Clases",
                "event_date": "2026-03-01",
                "description": "Periodo asociado a compras de útiles escolares, dispositivos tecnológicos y servicios educativos, con incremento de riesgos relacionados con fraudes digitales.",
                "risk_level": "HIGH",
            },
            {
                "name": "Venta de Garage Departamental",
                "event_date": "2026-08-15",
                "description": "Evento orientado a liquidaciones y descuentos especiales que incrementa la circulación de promociones digitales y la exposición a amenazas cibernéticas.",
                "risk_level": "MEDIUM",
            },
        ]

        for event_data in events_data:
            Event.objects.get_or_create(
                name=event_data["name"],
                defaults=event_data
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Seed ejecutado correctamente"
            )
        )

        # Buscar amenazas
        phishing = Threat.objects.get(name="Phishing")
        sitio_web_clonado = Threat.objects.get(name="Sitio Web Clonado")
        ingenieria_social = Threat.objects.get(name="Ingeniería Social")
        smishing = Threat.objects.get(name="Smishing")
        malware_promocional = Threat.objects.get(name="Malware Promocional")
        robo_sesion = Threat.objects.get(name="Robo de Sesión (Session Hijacking)")

        # Buscar eventos
        cyberday = Event.objects.get(name="Cyberday")
        black_friday = Event.objects.get(name="Black Friday")
        navidad = Event.objects.get(name="Navidad")
        dia_madre = Event.objects.get(name="Día de la Madre")
        fiestas_patrias = Event.objects.get(name="Fiestas Patrias")
        regreso_clases = Event.objects.get(name="Regreso a Clases")
        venta_garage = Event.objects.get(name="Venta de Garage Departamental")

        # Relaciones
        cyberday.threats.set([
            phishing,
            sitio_web_clonado,
            ingenieria_social,
        ])

        black_friday.threats.set([
            phishing,
            sitio_web_clonado,
            ingenieria_social,
        ])

        navidad.threats.set([
            phishing,
            sitio_web_clonado,
            ingenieria_social,
        ])

