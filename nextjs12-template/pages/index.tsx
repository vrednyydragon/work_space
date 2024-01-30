import type {GetServerSideProps, NextPage} from 'next'
import Layout from "../components/Layout";
import {getSession, signIn} from "next-auth/react";
import {Session} from "next-auth";


type Props = {
    session: Session | undefined,
    token: string | undefined,
}

const Home: NextPage<Props> = (props: Props) => {

    if (props.session?.error === "RefreshAccessTokenError") {
        signIn().then() // Force sign
    }

    return (
        <Layout title="Custom App">
            <div className="w-full min-h-screen bg-gray-50 flex flex-col sm:justify-center items-center pt-6 sm:pt-0">
                <span className="text-3xl font-bold underline text-blue-600">
                    Hello World!
                </span>
            </div>
        </Layout>
    )
}

export const getServerSideProps: GetServerSideProps = async (context) => {
    const session = await getSession(context)
    const {req, res} = context

    // const token: string | undefined = session?.user.access_token
    const token: string | unknown = session?.accessToken

    if (!session || !token || session?.error === "RefreshAccessTokenError") {

        return {
            redirect: {
                destination: '/api/auth/signin',
                permanent: false
            }
        }
    }

    return {
        props: {
            session,
            token
        },
    }
}


export default Home
