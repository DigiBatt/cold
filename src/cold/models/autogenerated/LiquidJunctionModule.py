
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalInterfaceModule import ElectrochemicalInterface







class LiquidJunction(ElectrochemicalInterface):
    """
    Class representing the `LiquidJunction` entity, which inherits from:
    - ElectrochemicalInterface

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_634467ad_feed_4979_adb2_877d98fe1768'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LiquidJunction'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LiquidJunction(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_634467ad_feed_4979_adb2_877d98fe1768',
    
    class_name='LiquidJunction',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_634467ad_feed_4979_adb2_877d98fe1768',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LiquidJunction',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    