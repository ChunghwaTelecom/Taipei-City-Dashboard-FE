import requests
import pandas as pd
from tqdm import tqdm
from typing import Dict, List
from sklearn.linear_model import LinearRegression
from urllib.parse import quote
from selenium import webdriver
from bs4 import BeautifulSoup


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
            map_box_geo_data = get_map_box_geo_data_from_address(row["addr"])
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
        input_df["dist"] = locality_texts

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
            map_box_geo_data = get_map_box_geo_data_from_address(row["addr"])
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
        input_df["dist"] = locality_texts

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
            map_box_geo_data = get_map_box_geo_data_from_address(row["addr"])
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
        input_df["dist"] = locality_texts

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

    @staticmethod
    def output_204_json(file_path: str):
        input_df: pd.DataFrame = pd.read_csv(file_path)
        input_df.drop(
            columns=[
                "id",
                "addr",
                "行政區碼",
                "center_longitude",
                "center_latitudes",
                "locality_ids",
            ]
        )
        new_order = [
            "dist",
            "name",
            "2017_rating",
            "2018_rating",
            "2019_rating",
            "2020_rating",
            "2021_rating",
            "2022_rating",
        ]
        input_df = input_df[new_order]
        input_df.fillna("", inplace=True)
        value_list = input_df.values.tolist()
        print(value_list)


class Crawler:
    def __init__(self):
        super().__init__()

    def get_hidden_value(
        self,
    ):
        response = requests.get("https://ap.ece.moe.edu.tw/webecems/pubSearch.aspx")
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        viewstate = soup.find("input", {"name": "__VIEWSTATE"}).get("value")
        eventvalidation = soup.find("input", {"name": "__EVENTVALIDATION"}).get("value")
        viewstatencrypted = soup.find("input", {"name": "__VIEWSTATEENCRYPTED"}).get(
            "value"
        )
        viewstategenerator = soup.find("input", {"name": "__VIEWSTATEGENERATOR"}).get(
            "value"
        )

        return viewstate, eventvalidation, viewstatencrypted, viewstategenerator

    def get_search_result(
        self, viewstate, eventvalidation, viewstatencrypted, viewstategenerator
    ):
        url = "https://ap.ece.moe.edu.tw/webecems/pubSearch.aspx"
        data = {
            "ScriptManager1": quote("UpdatePanel1|btnSearch"),
            "ddlKey": "",
            "txtKeyNameS": "財團法人林迺翁文教基金會附設臺北市私立天鵝堡幼兒園",
            "ddlCityS": "",
            "ddlAreaS": "",
            "hY": "",
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__EVENTVALIDATION": eventvalidation,
            "__LASTFOCUS": "",
            "__VIEWSTATE": viewstate,
            "__VIEWSTATEENCRYPTED": viewstatencrypted,
            "__VIEWSTATEGENERATOR": viewstategenerator,
            "__ASYNCPOST": "false",
            "btnSearch": quote("搜尋"),
        }
        response = requests.post(url, data=data)

        return response

    def crawl_the_cost(self, input_df: pd.DataFrame):
        (
            viewstate,
            eventvalidation,
            viewstatencrypted,
            viewstategenerator,
        ) = self.get_hidden_value()
        self.get_search_result(
            viewstate, eventvalidation, viewstatencrypted, viewstategenerator
        )

    def simulate_click(
        self,
    ):
        driver = webdriver.Chrome()

        # Open the webpage
        driver.get("URL_OF_THE_PAGE")

        # Find the submit button and click
        submit_button = driver.find_element_by_id("GridView1_btnMore_0")
        submit_button.click()

        # Now, you can access the new content loaded by the click
        # For example, you can get the page source:
        new_content = driver.page_source

        # Don't forget to close the browser
        driver.quit()


class FuturePredictor:
    def __init__():
        super().__init__()

    def predict(input_df):
        input_df["Year"] = input_df["Year"].astype(int)
        input_df["First Half"] = input_df["First Half"].str.replace(",", "").astype(int)
        input_df["Second Half"] = (
            input_df["Second Half"].str.replace(",", "").astype(int)
        )

        # Training linear regression models for 'First Half' and 'Second Half'
        model_first_half_new = LinearRegression()
        model_second_half_new = LinearRegression()

        model_first_half_new.fit(input_df[["Year"]], input_df["First Half"])
        model_second_half_new.fit(input_df[["Year"]], input_df["Second Half"])

        # Predicting for the years 113 to 117
        future_years_new = pd.DataFrame({"Year": [113, 114, 115, 116, 117]})
        future_years_new["First Half Predicted"] = model_first_half_new.predict(
            future_years_new[["Year"]]
        )
        future_years_new["Second Half Predicted"] = model_second_half_new.predict(
            future_years_new[["Year"]]
        )

        return future_years_new


def main():
    postpartum_care_center_file_path = (
        "data/raw_data/postpartum_care_center_with_money.csv"
    )
    summary_kindergarten_file_path = "data/raw_data/summary_kindergarten.csv"
    infant_daycare_center_file_path = "data/raw_data/infant_daycare_center.csv"

    # Postpartum Care Center
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
    # processed_infant_daycare_center_df: pd.DataFrame = (
    #     InfantDaycareCenter.parse_infant_daycare_center(infant_daycare_center_file_path)
    # )
    # InfantDaycareCenter.output_infant_daycare_center(processed_infant_daycare_center_df)
    infant_daycare_center_file_path = "data/clean_data/infant_daycare_center.csv"
    InfantDaycareCenter.output_204_json(infant_daycare_center_file_path)

    # crawler: Crawler = Crawler()
    # crawler.crawl_the_cost(processed_summary_kindergarten_df)


if __name__ == "__main__":
    main()
