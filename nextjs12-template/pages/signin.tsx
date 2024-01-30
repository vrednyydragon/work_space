import {getCsrfToken, getSession} from "next-auth/react"
import Head from 'next/head';
import {GetServerSideProps, NextPage,} from "next";
import {useRouter} from "next/router";

type Props = {
    csrfToken: string | undefined
}

type Errors = {
    Signin?: string,
    OAuthSignin?: string,
    OAuthCallback?: string,
    OAuthCreateAccount?: string,
    EmailCreateAccount?: string,
    Callback?: string,
    OAuthAccountNotLinked?: string,
    EmailSignin?: string,
    CredentialsSignin?: string,
    default?: string
}


const errors: Errors | any = {
    Signin: "Try signing with a different account.",
    OAuthSignin: "Try signing with a different account.",
    OAuthCallback: "Try signing with a different account.",
    OAuthCreateAccount: "Try signing with a different account.",
    EmailCreateAccount: "Try signing with a different account.",
    Callback: "Try signing with a different account.",
    OAuthAccountNotLinked:
        "To confirm your identity, sign in with the same account you used originally.",
    EmailSignin: "Check your email address.",
    CredentialsSignin:
        "Sign in failed. Check the details you provided are correct.",
    default: "Unable to sign in.",
};

const SignInError = ({error}: any): JSX.Element => {
    const errorMessage = error && (errors[error] ?? errors.default);
    return <div>{errorMessage}</div>;
};


const SignIn: NextPage<Props> = ({csrfToken}) => {

    const {error} = useRouter().query;

    return (
        <div>
            <Head>
                <title>Custom App</title>
            </Head>
            <div
                className={'w-full min-h-screen bg-cgray overscroll-none fixed'}>
                {/* error message if wrong email/password */}
                <div className={'absolute top-1/4 left-1/4 flex items-center text-center text-2xl font-bold'}>
                    {error &&
                        <SignInError error={error}/>}
                </div>
                <div
                    className={'bg-white shadow-md rounded-lg px-28 pt-8 pb-12 mb-4 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2'}>
                    <div className={'text-2xl mb-4'}>Custom App</div>
                    <form method="post" action="/api/auth/callback/credentials">

                        <input name="csrfToken" type="hidden" defaultValue={csrfToken}/>

                        <div className={'mb-4'}>
                            <input className={'login-input'} name="username" type="email" placeholder='E-mail'
                                   defaultValue={'user@mail.com'} required/>
                        </div>
                        <div className={'mb-6'}>
                            <input className={'login-input'} name="password" type="password" placeholder={'Password'}
                                   defaultValue={'super'} required/>
                        </div>
                        <div className={'flex items-center justify-end'}>
                            <button
                                className={'bg-green-500 hover:bg-green-700 text-white font-light py-2 px-4 rounded focus:outline-none focus:shadow-outline'}
                                type="submit">Login
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}


export const getServerSideProps: GetServerSideProps = async (context) => {
    const session = await getSession(context)
    const csrfToken = await getCsrfToken(context)
    const {req, res} = context

    if (session && res && session.accessToken && !session.error) {
        return {
            redirect: {
                destination: '/',
                permanent: false
            }
        }
    }

    return {
        props: {
            csrfToken,
        },
    }
}

// default stations
export default SignIn
