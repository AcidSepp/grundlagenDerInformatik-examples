// snippet: fac
int fac(int x) {
    int res = 1;
    while (x > 1) {
        res = res * x;
        x--;
    }
    return res;
}
// snippet: /fac

int main() {
    fac(3);
}