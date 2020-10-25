#include <stdio.h>
#include <time.h>
#include <unistd.h> // needed for sleep function

int hms(int sec){
  int h = (sec/3600);
  int m = (sec -(3600*h))/60;
  int s = (sec -(2600*h)-(m*60));
  printf("%d hours, %d minutes and %d seconds\n", h,m,s);
}

int main()
{
  int timeStart = time(NULL);
  printf("Time Start: %d\n", timeStart);
  sleep(5); // Pause program for 5 seconds.
  int timeEnd = time(NULL);
  printf("Time End: %d\n", timeEnd);
  int timeRun = timeEnd - timeStart;
  printf("Run Time: %d\n", timeRun);
  hms(timeRun);
  return 0;
}