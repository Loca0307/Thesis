//The quick sort was adapted from this youtube video
//I want to eventually remake this in my own unique code
//https://www.youtube.com/watch?v=Vtckgz38QHs
int Partition(vector<int>& arr, int startIndex, int endIndex)
{
	int pivot = arr[endIndex];
	int i = startIndex - 1;

	for (int j = startIndex; j <= endIndex - 1; j++)
	{
		if (arr[j] < pivot)
		{
			i++;
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}
	i++;
	int temp = arr[i];
	arr[i] = arr[endIndex];
	arr[endIndex] = temp;

	return i;
}
void QuickSorting(vector<int>& arr, int startIndex, int endIndex)
{
	if (endIndex <= startIndex) return;

	int pivot = Partition(arr, startIndex, endIndex);
	QuickSorting(arr, startIndex, pivot - 1);
	QuickSorting(arr, pivot + 1, endIndex);

	isQuickTrue = false;
}

//The insertion sort was adapted from this youtube video
//I want to eventually remake this in my own unique code
//https://www.youtube.com/watch?v=8mJ-OhcfpYg
void InsertionSorting(vector<int>& arr)