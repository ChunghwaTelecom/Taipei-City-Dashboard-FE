import requests
import pandas as pd
from tqdm import tqdm
from typing import Dict, List
from urllib.parse import quote


def get_map_box_geo_data_from_address(actural_address: str) -> Dict[str, object]:
    map_box_geo_data = {}
    map_box_access_token: str = "pk.eyJ1IjoiZXJpY3p4MTAzNzAzMDEyIiwiYSI6ImNscDNqNTlnNTEydXkyanF5emtzc296MmkifQ.eRRCu7Zxrx3MydV_yVjG8Q"  # noqa
    encoded_actural_address: str = quote(actural_address)

    target_url: str = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{encoded_actural_address}.json?access_token={map_box_access_token}"  # noqa

    response = requests.get(target_url)
    if response.status_code == 200:
        data = response.json()

        if "features" in data and len(data["features"]) > 0:
            map_box_geo_data["center_longitude"] = data["features"][0]["center"][0]
            map_box_geo_data["center_latitude"] = data["features"][0]["center"][1]
            map_box_geo_data["locality_id"] = data["features"][0]["context"][2]["id"]
            map_box_geo_data["locality_text"] = data["features"][0]["context"][2][
                "text"
            ]
        else:
            map_box_geo_data["center_longitude"] = data["features"][0]["center"][0]
            map_box_geo_data["center_latitude"] = data["features"][0]["center"][1]
            map_box_geo_data["locality_id"] = data["features"][0]["context"][2]["id"]
            map_box_geo_data["locality_text"] = data["features"][0]["context"][2][
                "text"
            ]

        return map_box_geo_data
    else:
        return map_box_geo_data


class PostpartumCareCenterProcessor:
    def __init__():
        super().__init__()

    @staticmethod
    def parse_postpartum_care_center(file_path: str) -> pd.DataFrame:
        input_df: pd.DataFrame = pd.read_csv(file_path)

        map_box_geo_data_list: List[Dict[str, object]] = []

        for _, row in tqdm(input_df.iterrows()):
            map_box_geo_data = get_map_box_geo_data_from_address(row["機構地址"])
            map_box_geo_data_list.append(map_box_geo_data)

        center_longitudes = [
            map_box_geo_data["center_longitude"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        center_latitudes = [
            map_box_geo_data["center_latitude"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        locality_ids = [
            map_box_geo_data["locality_id"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        locality_texts = [
            map_box_geo_data["locality_text"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        input_df["center_longitude"] = center_longitudes
        input_df["center_latitudes"] = center_latitudes
        input_df["locality_ids"] = locality_ids
        input_df["locality_texts"] = locality_texts

        return input_df

    @staticmethod
    def output_postpartum_care_center(processed_df: pd.DataFrame):
        processed_df.to_csv(
            "data/clean_data/processed_postpartum_care_center.csv", index=False
        )
        processed_json = processed_df.to_json(orient="records", force_ascii=False)
        with open(
            "data/clean_data/processed_postpartum_care_center.json",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(processed_json)


class SummaryKindergarten:
    def __init__():
        super().__init__()

    @staticmethod
    def parse_summary_kindergarten(file_path: str) -> pd.DataFrame:
        input_df: pd.DataFrame = pd.read_csv(file_path)

        map_box_geo_data_list: List[Dict[str, object]] = []

        for _, row in tqdm(input_df.iterrows()):
            map_box_geo_data = get_map_box_geo_data_from_address(row["幼兒園住址"])
            map_box_geo_data_list.append(map_box_geo_data)

        center_longitudes = [
            map_box_geo_data["center_longitude"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        center_latitudes = [
            map_box_geo_data["center_latitude"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        locality_ids = [
            map_box_geo_data["locality_id"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        locality_texts = [
            map_box_geo_data["locality_text"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        input_df["center_longitude"] = center_longitudes
        input_df["center_latitudes"] = center_latitudes
        input_df["locality_ids"] = locality_ids
        input_df["locality_texts"] = locality_texts

        return input_df

    @staticmethod
    def output_summary_kindergarten(processed_df: pd.DataFrame):
        processed_df.to_csv("data/clean_data/summary_kindergarten.csv", index=False)
        processed_json = processed_df.to_json(orient="records", force_ascii=False)
        with open(
            "data/clean_data/summary_kindergarten.json",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(processed_json)


class InfantDaycareCenter:
    def __init__():
        super().__init__()

    @staticmethod
    def parse_infant_daycare_center(file_path: str) -> pd.DataFrame:
        input_df: pd.DataFrame = pd.read_csv(file_path)

        map_box_geo_data_list: List[Dict[str, object]] = []

        for _, row in tqdm(input_df.iterrows()):
            map_box_geo_data = get_map_box_geo_data_from_address(row["機構地址"])
            map_box_geo_data_list.append(map_box_geo_data)

        center_longitudes = [
            map_box_geo_data["center_longitude"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        center_latitudes = [
            map_box_geo_data["center_latitude"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        locality_ids = [
            map_box_geo_data["locality_id"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        locality_texts = [
            map_box_geo_data["locality_text"]
            for map_box_geo_data in map_box_geo_data_list
        ]

        input_df["center_longitude"] = center_longitudes
        input_df["center_latitudes"] = center_latitudes
        input_df["locality_ids"] = locality_ids
        input_df["locality_texts"] = locality_texts

        return input_df

    @staticmethod
    def output_infant_daycare_center(processed_df: pd.DataFrame):
        processed_df.to_csv("data/clean_data/infant_daycare_center.csv", index=False)
        processed_json = processed_df.to_json(orient="records", force_ascii=False)
        with open(
            "data/clean_data/infant_daycare_center.json",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(processed_json)


def main():
    postpartum_care_center_file_path = (
        "data/raw_data/postpartum_care_center_with_money.csv"
    )
    summary_kindergarten_file_path = "data/raw_data/summary_kindergarten.csv"
    infant_daycare_center_file_path = "data/raw_data/infant_daycare_center.csv"

    # # Postpartum Care Center
    # processed_postpartum_care_center_df: pd.DataFrame = (
    #     PostpartumCareCenterProcessor.parse_postpartum_care_center(
    #         postpartum_care_center_file_path
    #     )
    # )
    # PostpartumCareCenterProcessor.output_postpartum_care_center(
    #     processed_postpartum_care_center_df
    # )

    # # Summary Kindergarten
    # processed_summary_kindergarten_df: pd.DataFrame = (
    #     SummaryKindergarten.parse_summary_kindergarten(summary_kindergarten_file_path)
    # )
    # SummaryKindergarten.output_summary_kindergarten(processed_summary_kindergarten_df)

    # Infant Daycare Center
    processed_infant_daycare_center_df: pd.DataFrame = (
        InfantDaycareCenter.parse_infant_daycare_center(infant_daycare_center_file_path)
    )
    InfantDaycareCenter.output_infant_daycare_center(processed_infant_daycare_center_df)


if __name__ == "__main__":
    main()
