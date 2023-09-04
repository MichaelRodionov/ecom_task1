class Service:
    """
    Service class for business logic
    """
    data = None

    def get_results(self, data: list) -> dict:
        """
        Method to prepare result response
        """
        self.data = data
        return {
            'Процент пустых характеристик': self.count_null_percent(),
            "Количество символов в атрибуте 'Аннотация'": self.count_symbols(),
            "Количество фото в атрибуте 'images'": self.count_img()
        }

    def count_null_percent(self) -> float:
        """
        Method to count percentage of non-filled characteristics
        """
        char_count: int = 0
        null_count: int = 0
        for obj in self.data:
            for char in obj:
                if char in ["", 'NULL']:
                    null_count += 1
            char_count += len(obj)
        return round((null_count / char_count) * 100, 1)

    def count_symbols(self) -> int:
        """
        Method to count symbols in attribute 'Аннотация'
        """
        for obj in self.data:
            if 'Аннотация' in obj:
                return len(obj[len(obj)-1])

    def count_img(self) -> int | None:
        """
        Method to count symbols in attribute 'images'
        """
        for obj in self.data:
            if 'images' in obj:
                return len([img_url for img_url in obj[len(obj)-1].split(';') if img_url.endswith('.jpg')])

