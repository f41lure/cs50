#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    int jpg_ctr = 0;                                                    // A counter to keep track of jpegs
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover file or sample\n");
        return 1;
    }

    // remember filenames
    char *pfile_n = argv[1];

    // open input file
    FILE *pfile = fopen(pfile_n, "r");
    if (pfile == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", pfile_n);
        return 2;
    }
    BYTE iter[512];
    FILE *jpeg = NULL;                                                  // A file for JPEGS
    char jpegn[10];

    // BTW, fread(iter, 512, 1, pfile)==1 would **not** work!
    while (!feof(pfile))                                                // While EOF == false...
    {
        if (iter[0] == 0xff && iter[1] == 0xd8 && iter[2] == 0xff && (iter[3] & 0xf0) == 0xe0)      // Demarcating the beginning of a JPEG
        {
            if (jpeg != NULL)
            {
                fclose(jpeg);
            }
            sprintf(jpegn, "%03d.jpg", jpg_ctr);                        // Filenames
            jpeg = fopen(jpegn, "w");
            jpg_ctr++;                                                  // Increment JPEG counter
            fwrite(iter, sizeof(iter), 1, jpeg);
        }
        else if (jpg_ctr > 0)
        {
            fwrite(iter, sizeof(iter), 1, jpeg);
        }
        fread(iter, sizeof(iter), 1, pfile);
    }

    // close infile
    fclose(pfile);

    // success
    return 0;
}
