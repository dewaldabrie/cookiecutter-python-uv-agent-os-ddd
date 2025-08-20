"""NiceGUI frontend for {{cookiecutter.project_name}}"""

from nicegui import ui


def main_page():
    """Main page of the application"""
    with ui.card():
        ui.label('Welcome to {{cookiecutter.project_name}}')
        ui.label('{{cookiecutter.main_idea}}').classes('text-sm text-gray-600')
        
        with ui.expansion('Key Features').classes('w-full'):
            features = '{{cookiecutter.key_features}}'.split(', ')
            for feature in features:
                ui.label(f'• {feature}')
        
        with ui.expansion('Target Users').classes('w-full'):
            ui.label('{{cookiecutter.target_users}}')


def run():
    """Run the NiceGUI application"""
    main_page()
    ui.run(title='{{cookiecutter.project_name}}')


if __name__ in {'__main__', '__mp_main__'}:
    run()