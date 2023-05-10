# System imports
import os
import sys

# ArcGIS imports
import arcpy

# Local imports
# Add Scripts folder to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import FLM_Tools


def main():
    """ This is an example script for calling FLM tools for processing single dataset"""

    # Set arcpy environment variables
    arcpy.env.overwriteOutput = True

    # Coordinate Reference System: NAD 1983 10TM AEP Forest
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(2956)

    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")

    # Example for whole workflow
    baseDir = r"D:\Line_Editing\Kirby_2022\Test_DLP"
    resultDir = r"D:\Line_Editing\Kirby_2022\Test_DLP"

    in_chm = os.path.join(baseDir, r"CHM_Kirby_SiteK.tif")
    in_line = os.path.join(baseDir, r"seedpoints_SiteK.shp")
    in_canopy_raster = os.path.join(baseDir, r"Canopy_SiteK.tif")
    in_cost_raster = os.path.join(baseDir, r"Cost_SiteK.tif")
    in_lidar_year = os.path.join(baseDir, r"LiDAR_Tiles_with_Year.shp")
    out_tagged_line = os.path.join(resultDir, r"Tag_Line_out_tagged.shp")
    out_centerline = os.path.join(resultDir, r"centerline_SiteK.shp")
    out_line_optimized = os.path.join(resultDir, r"In_Line_SiteK_VO.shp")
    out_footprint = os.path.join(resultDir, r"footprint_SiteK.shp")
    out_footprint_dyn = os.path.join(resultDir, r"footprint_SiteK_Dyn.shp")
    out_attribute_whole = os.path.join(resultDir, r"Tag_Attr_whole.shp")  # WHOLE-LINE
    out_attribute_arbitrary = os.path.join(resultDir, r"Tag_Attr_arbitrary.shp")  # ARBITRARY
    out_attribute_in_features = os.path.join(resultDir, r"Tag_Attr_in_features.shp")  # IN-FEATURES
    out_attribute_line_crossings = os.path.join(resultDir, r"Tag_Attr_line_crossings.shp")  # LINE-CROSSINGS

    # FLM_Tools.preTagging(in_line, in_chm, in_canopy_raster, in_cost_raster, in_lidar_year, out_tagged_line)
    # FLM_Tools.vertexOptimization(in_line, in_cost_raster, out_line_optimized)
    FLM_Tools.centerline(in_line, in_cost_raster, out_centerline)
    FLM_Tools.lineFootprint(out_centerline, in_canopy_raster, in_cost_raster, out_footprint, corridor_threshold=5)
    FLM_Tools.dynamicLineFootprint(out_centerline, in_chm, out_footprint_dyn)

    # FLM_Tools.lineAttribute("WHOLE-LINE", out_centerline, out_footprint, in_chm, out_attribute_whole)
    # FLM_Tools.lineAttribute("ARBITRARY", out_centerline, out_footprint, in_chm, out_attribute_arbitrary)
    # FLM_Tools.lineAttribute("IN-FEATURES", out_centerline, out_footprint, in_chm, out_attribute_in_features)
    # FLM_Tools.lineAttribute("LINE-CROSSINGS", out_centerline, out_footprint, in_chm, out_attribute_line_crossings)

    # Use json as batch processing parameter input
    # import json
    #
    # with open(r"D:\FLM_Sensituvity_Test\footprint_below2m.json") as json_file:
    #     params = json.load(json_file)
    #
    #     for i in params:
    #         FLM_Tools.lineFootprint(i["in_line"], i["canopy_raster"], i["cost_raster"],
    #                                 i["out_footprint"], max_line_width=i["line_width"])

if __name__ == "__main__":
    main()
