#include <iostream>
#include <windows.h>
#include <gdiplus.h>
#include <vector>
#include <fstream>

using namespace Gdiplus;

#include "classes/texturemap.hpp"

//Linkers: -lgdi32 -lgdiplus

ULONG_PTR gdiplusToken;
std::vector<texturemap> textureMaps;

void addTexturemap(const wchar_t* path, std::string name) {
    texturemap tmpMap;
    tmpMap.setMap(new Bitmap(path));
    Rect box(0, 0, tmpMap.getMap()->GetWidth(), tmpMap.getMap()->GetHeight());
    tmpMap.getMap()->LockBits(&box, ImageLockModeRead, PixelFormat24bppRGB, &tmpMap.getMapData());
    tmpMap.setMapPixels(static_cast<BYTE*>(tmpMap.getMapData().Scan0));
    tmpMap.getName() = name;
    textureMaps.emplace_back(tmpMap);
}

void loadTexturemaps() {
    addTexturemap(L"icon.bmp", "icon");
}

int main() {
    GdiplusStartupInput gdiplusStartupInput = {0};
    GdiplusStartup(&gdiplusToken, &gdiplusStartupInput, NULL);

    loadTexturemaps();

    std::ofstream file("out.icon");
    if (!file.is_open()) {
        system("cls");
        std::cout << "frame.bmp could not be found. Press enter to exit.\n";
        return 1;
    }

    for (int y = 0; y < textureMaps[0].getMap()->GetHeight(); y++) {
        for (int x = 0; x < textureMaps[0].getMap()->GetWidth(); x++) {
            int index = (y * textureMaps[0].getMapData().Stride + (x * 3));
                int red = static_cast<int>(textureMaps[0].getMapPixels()[index + 2]);
                int green = static_cast<int>(textureMaps[0].getMapPixels()[index + 1]);
                int blue = static_cast<int>(textureMaps[0].getMapPixels()[index]);

                if ((red + green + blue) > 0) {
                    file << x << "," << y << "\n";
                }
        }
    }

    file.close();

    GdiplusShutdown(gdiplusToken);
    return 0;
}
