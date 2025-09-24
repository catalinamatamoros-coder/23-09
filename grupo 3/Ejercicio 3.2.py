#!/usr/bin/env python3
# agenda.py
import json
import os
import re

AGENDA_FILE = "agenda.json"

def load_agenda():
    if os.path.exists(AGENDA_FILE):
        try:
            with open(AGENDA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            print("Advertencia: no se pudo leer agenda.json (archivo vacío o corrupto). Se inicia una agenda nueva.")
    return {}

def save_agenda(agenda):
    try:
        with open(AGENDA_FILE, 'w', encoding='utf-8') as f:
            json.dump(agenda, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Error guardando agenda:", e)

def normalize(name):
    return name.strip().lower()

def valid_phone(phone):
    return bool(re.match(r'^[\d\+\-\s\(\)]+$', phone.strip()))

def add_contact(agenda):
    name = input("Nombre: ").strip()
    if not name:
        print("Nombre vacío. Operación cancelada.")
        return
    key = normalize(name)
    phone = input("Teléfono: ").strip()
    if not phone:
        print("Teléfono vacío. Operación cancelada.")
        return
    if not valid_phone(phone):
        print("Formato teléfono: sólo dígitos, +, -, paréntesis y espacios son permitidos, pero se guardará igual.")
    if key in agenda:
        current = agenda[key]
        print(f"Ya existe '{current['name']}' -> {current['phone']}")
        ans = input("¿Sobrescribir? (s/n): ").strip().lower()
        if ans not in ('s', 'si', 'y', 'yes'):
            print("No se modificó el contacto.")
            return
    agenda[key] = {'name': name, 'phone': phone}
    print(f"Contacto '{name}' guardado.")

def search_contact(agenda):
    q = input("Buscar nombre (puede ser parcial): ").strip().lower()
    if not q:
        print("Búsqueda vacía.")
        return
    matches = [v for k,v in agenda.items() if q in k]
    if not matches:
        print("No se encontraron contactos.")
        return
    print(f"Se encontraron {len(matches)} contacto(s):")
    for i, c in enumerate(matches, 1):
        print(f"{i}. {c['name']} — {c['phone']}")

def delete_contact(agenda):
    q = input("Nombre a eliminar (o parcial): ").strip().lower()
    if not q:
        print("Entrada vacía.")
        return
    matches = [(k,v) for k,v in agenda.items() if q in k]
    if not matches:
        print("No se encontraron contactos.")
        return
    if len(matches) == 1:
        k, v = matches[0]
        ans = input(f"Eliminar '{v['name']}' ({v['phone']})? (s/n): ").strip().lower()
        if ans in ('s', 'si', 'y', 'yes'):
            del agenda[k]
            print("Eliminado.")
        else:
            print("Cancelado.")
    else:
        print("Contactos encontrados:")
        for idx, (k,v) in enumerate(matches, 1):
            print(f"{idx}. {v['name']} — {v['phone']}")
        try:
            choice = int(input("Número a eliminar (0 para cancelar): "))
            if choice == 0:
                print("Cancelado.")
                return
            if 1 <= choice <= len(matches):
                del agenda[matches[choice-1][0]]
                print("Eliminado.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

def show_all(agenda):
    if not agenda:
        print("Agenda vacía.")
        return
    print("Agenda completa:")
    for v in sorted(agenda.values(), key=lambda x: x['name'].lower()):
        print(f"- {v['name']} : {v['phone']}")

def main():
    agenda = load_agenda()
    while True:
        print("\n--- Agenda ---")
        print("1) Añadir contacto")
        print("2) Buscar contacto")
        print("3) Eliminar contacto")
        print("4) Mostrar todos")
        print("5) Guardar y salir")
        print("6) Salir sin guardar")
        choice = input("Elige una opción (1-6): ").strip()
        if choice == '1':
            add_contact(agenda)
        elif choice == '2':
            search_contact(agenda)
        elif choice == '3':
            delete_contact(agenda)
        elif choice == '4':
            show_all(agenda)
        elif choice == '5':
            save_agenda(agenda)
            print("Guardado en", AGENDA_FILE)
            break
        elif choice == '6':
            ans = input("¿Salir sin guardar? (s/n): ").strip().lower()
            if ans in ('s', 'si', 'y', 'yes'):
                break
        else:
            print("Opción inválida.")
    print("Adiós.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrumpido. Saliendo...")