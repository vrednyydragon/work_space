import NextAuth from 'next-auth'
import CredentialsProvider from "next-auth/providers/credentials";


export default NextAuth({
    providers: [
        CredentialsProvider({
            // @ts-ignore
            options: undefined,
            // The name to display on the sign in form (e.g. "Sign in with...")
            name: "Credentials",


            // custom auth without connection to db
            // @ts-ignore
            async authorize(credentials, req) {
                // Add logic here to look up the user from the credentials supplied
                const userDb = {id: 1, name: "User", email: "user@mail.com", password: 'password'}
                const userRes = {
                    // it's not secure, but it's just an example, this is not a real token
                    access_token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQG1haWwuY29tIiwiZXhwIjoxNjUyOTU2Mzc1LCJuYW1lIjoidXNlciIsInJvbGUiOiJzdXBlciJ9.bBfq0uhLHoTFuAA7gpp7bORqWRMVkE2aBzG8Zykb0N8',
                    token_type: 'bearer',
                    token_expire: '2052-05-19T10:32:55.438890+00:00'
                }

                if (credentials?.username === userDb.email && credentials?.password === userDb.password) {
                    return userRes
                }

                // login failed
                return null
            }

            // // user authorization with using fastAPI endpoint and db
            // async authorize(credentials, req) {
            //
            //     if (credentials) {
            //
            //         // send form to endpoint and get response
            //         const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/users/login/`, {
            //             method: 'POST',
            //             body: JSON.stringify(credentials),
            //             headers: {"Content-Type": "application/json"}
            //         })
            //
            //         // get user data
            //         const user = await res.json()
            //
            //         // If no error and we have user data, return it
            //         if (res.ok && user) {
            //             return user
            //         }
            //     }
            //
            //     // Return null if user data could not be retrieved
            //     return null
            // }
        })
    ],
    secret: process.env.NEXTAUTH_SECRET,
    session: {
        strategy: 'jwt',
    },
    jwt: {
        secret: process.env.NEXTAUTH_SECRET,
    },

    callbacks: {

        async jwt({token, user}) {

            if (user) {
                // @ts-ignore
                token.accessToken = user.access_token
            }

            return token
        },

        async session({session, token}) {

            if (token) {
                session.token = token
                session.accessToken = token.accessToken

                // @ts-ignore
                const expToken = Date.parse(session.user.token_expire)

                if (Date.now() > (expToken)) {
                    session.error = "RefreshAccessTokenError"
                }
            }

            return session
        },

    },
    pages: {
        signIn: '/signin',

        // // other pages can be added to project
        // signOut: '/auth/signout',
        // error: '/auth/error', // Error code passed in query string as ?error=
        // verifyRequest: '/auth/verify-request', // (used for check email message)
        // newUser: '/auth/new-user' // New users will be directed here on first sign in (leave the property out if not of interest)
    }

})


