# 代码生成时间: 2025-10-02 19:37:42
import streamlit as st
def hello():
    st.write("Hello, World!")

class ServiceRegistry:
    """ A simple service registry for discovery and registration of services."""
    def __init__(self):
        self.services = {}

    def register_service(self, service_name, service_endpoint):
        """ Register a new service with the given name and endpoint.
        Args:
            service_name (str): The name of the service to register.
            service_endpoint (str): The endpoint of the service to register.
        Raises:
            ValueError: If the service is already registered.
        """
        if service_name in self.services:
            raise ValueError(f"Service '{service_name}' is already registered.")
        self.services[service_name] = service_endpoint
        st.write(f"Service '{service_name}' registered with endpoint '{service_endpoint}'.")

    def discover_service(self, service_name):
        """ Discover a service by name.
        Args:
            service_name (str): The name of the service to discover.
        Returns:
            str: The endpoint of the discovered service, or None if not found.
        """
        endpoint = self.services.get(service_name)
        if not endpoint:
            st.error(f"Service '{service_name}' not found.")
            return None
        st.write(f"Service '{service_name}' discovered with endpoint '{endpoint}'.")
        return endpoint

    def list_services(self):
        """ List all registered services.
        Returns:
            dict: A dictionary of all registered services with their endpoints.
        """
        return self.services

# Streamlit app logic
if __name__ == '__main__':
    st.title('Service Registry App')
    service_registry = ServiceRegistry()
    
    with st.form(key='service_form'):
        name = st.text_input('Service Name')
        endpoint = st.text_input('Service Endpoint')
        submit_button = st.form_submit_button(label='Register Service')
    
    if submit_button:
        try:
            service_registry.register_service(name, endpoint)
        except ValueError as e:
            st.error(e)
    
    discover_button = st.button('Discover Service')
    service_name_to_discover = st.text_input('Enter Service Name to Discover')
    if discover_button:
        service_registry.discover_service(service_name_to_discover)
    
    list_services_button = st.button('List All Services')
    if list_services_button:
        services = service_registry.list_services()
        for name, endpoint in services.items():
            st.write(f'Service Name: {name}, Endpoint: {endpoint}')