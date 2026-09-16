// snippet: fac
int fac(int n) {
    if (n == 1) {
        return 1;
    } else {
        return n*fac(n-1);
    }
}
// snippet: /fac

int main() {
    fac(3);
}