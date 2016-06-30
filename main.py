
import astropy.io.fits
import os


datafolder = 'data'
targetfolder = 'output'


def do_something(input_file, output_file, factor=10):
    data = astropy.io.fits.getdata(input_file)
    divided = data / factor
    astropy.io.fits.writeto(output_file, divided)


def so_something_on_folder(input_, output_, factor, pattern):
    for filename in os.listdir(input_):
        if filename.lower().endswith('.fits'):
            output_file = os.path.join(output_, filename)
            input_file = os.path.join(datafolder, filename)
            do_something(input_file, output_file, factor)


if __name__ == '__main__':
    so_something_on_folder(datafolder, targetfolder, factor=10, pattern='*.fits')
