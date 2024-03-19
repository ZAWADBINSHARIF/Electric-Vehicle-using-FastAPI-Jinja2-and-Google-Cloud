// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";

const signup_btn = document.getElementById("signup-btn");
const login_btn = document.getElementById("login-btn");
const logout = document.getElementById('logout');

const firebaseConfig = {
    apiKey: "AIzaSyDRdZr53xComz4lEeOdYkwct-2-x8U_a_k",
    authDomain: "electric-vehicles-7f208.firebaseapp.com",
    projectId: "electric-vehicles-7f208",
    storageBucket: "electric-vehicles-7f208.appspot.com",
    messagingSenderId: "147391266896",
    appId: "1:147391266896:web:78ceecce0f52a9e1da5155",
    measurementId: "G-Q2R3QKS4R3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

if (logout)
    logout.addEventListener('click', async () => {
        try {
            await signOut(auth);
            document.cookie = `token=;path=/;SameSite=Strict`;
            window.location.reload()
        } catch (error) {
            console.log(error);
        }
    }
    );

if (login_btn)
    login_btn.addEventListener('click', async e => {
        e.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        if (!email && !password)
            return;

        try {
            const response = await signInWithEmailAndPassword(auth, email, password);

            const token = response._tokenResponse.idToken;
            document.cookie = `token=${token};path=/;SameSite=Strict`;

            setTimeout(() => {
                window.location = "/";
            }, 1000)

            
        } catch (error) {
            console.log(error);
        }

    });

if (signup_btn)
    signup_btn.addEventListener('click', async e => {
        e.preventDefault();

        const email = document.getElementById("signup-email").value;
        const password = document.getElementById("signup-password").value;

        if (!email && !password)
            return;

        try {
            await createUserWithEmailAndPassword(auth, email, password);

            window.location = "/login";

        } catch (error) {
            console.log(error);
        }

    });
