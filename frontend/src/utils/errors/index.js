export function showErrorPage(errorCode) {
    window.location.replace('/error/' + errorCode.toString());
}