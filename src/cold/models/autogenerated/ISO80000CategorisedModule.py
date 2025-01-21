
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CategorizedPhysicalQuantityModule import CategorizedPhysicalQuantity







class ISO80000Categorised(CategorizedPhysicalQuantity):
    """
    Class representing the `ISO80000Categorised` entity, which inherits from:
    - CategorizedPhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2ce04004_62cf_4394_b6a2_b45fce1aebfe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ISO80000Categorised'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ISO80000Categorised(
    
    class_iri='https://w3id.org/emmo#EMMO_2ce04004_62cf_4394_b6a2_b45fce1aebfe',
    
    class_name='ISO80000Categorised',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2ce04004_62cf_4394_b6a2_b45fce1aebfe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ISO80000Categorised',
        alias="class_name"
    )
    

    
    

    

    