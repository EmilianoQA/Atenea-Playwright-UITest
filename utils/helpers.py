from playwright.sync_api import Response
import json


def validar_respuesta_api_simple(
    response: Response, expected_method: str, expected_status: int, expected_key: str
):
    """
    Realiza las 3 validaciones de API más importantes y directas:
    1. El método HTTP de la petición.
    2. El código de estado de la respuesta.
    3. La existencia de una clave principal en el cuerpo JSON.
    """
    print(
        f"Validando API: Método='{expected_method}', Status='{expected_status}', Clave='{expected_key}'"
    )

    # 1. Validar el método
    assert (
        response.request.method == expected_method
    ), f"El método esperado era '{expected_method}', pero se recibió '{response.request.method}'"

    # 2. Validar el código de estado
    assert (
        response.status == expected_status
    ), f"El status esperado era {expected_status}, pero se recibió {response.status}"

    # 3. Validar la clave de relevancia en el cuerpo
    try:
        body = response.json()
        assert (
            expected_key in body
        ), f"La clave '{expected_key}' no se encontró en el cuerpo de la respuesta."
    except json.JSONDecodeError:
        assert False, "Error: El cuerpo de la respuesta no es un JSON válido."

    print("✅ Validación de API exitosa.")
    return body
