
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalBosonModule import FundamentalBoson







class GaugeBoson(FundamentalBoson):
    """
    Class representing the `GaugeBoson` entity, which inherits from:
    - FundamentalBoson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fd6559e8_ef94_460c_9dfc_bad5c68d63b4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GaugeBoson'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GaugeBoson(
    
    class_iri='https://w3id.org/emmo#EMMO_fd6559e8_ef94_460c_9dfc_bad5c68d63b4',
    
    class_name='GaugeBoson',
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fd6559e8_ef94_460c_9dfc_bad5c68d63b4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GaugeBoson',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    