
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class CRate(RatioQuantity, ElectrochemicalQuantity):
    """
    Class representing the `CRate` entity, which inherits from:
    - RatioQuantity, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e1fd84eb_acdb_4b2c_b90c_e899d552a3ee'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CRate'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CRate(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e1fd84eb_acdb_4b2c_b90c_e899d552a3ee',
    
    class_name='CRate',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e1fd84eb_acdb_4b2c_b90c_e899d552a3ee',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CRate',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    