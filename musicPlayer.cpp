int sewuence(int n)
{
    int sum_of_sequance = 0;
    int i = 1;
    int sequance_no = 0;
    while (i <= n)
    {
        sequance_no = (sequance_no * 10) + 1;
        sum_of_sequance += sequance_no;
        i += 1;
    }
    return sum_of_sequance;
}