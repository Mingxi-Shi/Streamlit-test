# Done by Muench
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from resources.user_credentials.hasher import Hasher
from resources.user_credentials.authenticate import Authenticate


def main():
    st.set_page_config(page_title="用户登录器", page_icon="🌸", layout="wide")

    sysmenu = '''
                <style>
                #MainMenu {visibility:hidden;}
                footer {visibility:hidden;}
                '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    with open('resources/user_credentials/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    name, authentication_status, username = authenticator.login('Login', 'main')
    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        st.title('Some content')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

    # # Creating a password reset widget
    # if authentication_status:
    #     try:
    #         if authenticator.reset_password(username, 'Reset password'):
    #             st.success('Password modified successfully')
    #     except Exception as e:
    #         st.error(e)
    #
    # # Creating a new user registration widget
    # try:
    #     if authenticator.register_user('Register user', preauthorization=False):
    #         st.success('User registered successfully')
    # except Exception as e:
    #     st.error(e)
    #
    # # Creating a forgot password widget
    # try:
    #     username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
    #     if username_forgot_pw:
    #         st.success('New password sent securely')
    #         # Random password to be transferred to user securely
    #     elif username_forgot_pw == False:
    #         st.error('Username not found')
    # except Exception as e:
    #     st.error(e)
    #
    # # Creating a forgot username widget
    # try:
    #     username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
    #     if username_forgot_username:
    #         st.success('Username sent securely')
    #         # Username to be transferred to user securely
    #     elif username_forgot_username == False:
    #         st.error('Email not found')
    # except Exception as e:
    #     st.error(e)
    #
    # # Creating an update user details widget
    # if authentication_status:
    #     try:
    #         if authenticator.update_user_details(username, 'Update user details'):
    #             st.success('Entries updated successfully')
    #     except Exception as e:
    #         st.error(e)
    #
    # # Saving config file
    # with open('resources/user_credentials/config.yaml', 'w') as file:
    #     yaml.dump(config, file, default_flow_style=False)


if __name__ == '__main__':
    main()