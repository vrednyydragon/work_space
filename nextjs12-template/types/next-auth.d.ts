declare module "next-auth" {
    /**
     * Returned by `useSession`, `getSession` and received as a prop on the `SessionProvider` React Context
     */
    interface Session {
        user: {
            access_token: string,
            token_type: string,
            token_expire: string | undefined
        },
        token: JWT,
        accessToken: string | unknown,
        error: string
    }
}
