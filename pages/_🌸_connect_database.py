# Done by Muench
import streamlit as st


def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            # st.session_state["password"]  # don't store username + password
            # st.session_state["username"]
            st.session_state.a = st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True


def main():
    print(1)
    st.write(1)
    st.write(2)
    # https://docs.streamlit.io/knowledge-base/tutorials/databases/mssql
    # https://docs.streamlit.io/knowledge-base/tutorials/databases/mysql
    # 使用数据库的账号和密码登录
    # 显示内容
    # if check_password():
    #     st.write("Here goes your normal Streamlit app...")
    #     st.button("Click me")
    #     st.write("user ", st.session_state.a, "has login in")


if __name__ == '__main__':
    main()



# https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management
# https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso