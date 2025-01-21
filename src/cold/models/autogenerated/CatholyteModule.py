
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LiquidElectrolyteModule import LiquidElectrolyte







class Catholyte(LiquidElectrolyte):
    """
    Class representing the `Catholyte` entity, which inherits from:
    - LiquidElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_15b852b5_19cc_49ab_849f_7df6175fb2be'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Catholyte'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Catholyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_15b852b5_19cc_49ab_849f_7df6175fb2be',
    
    class_name='Catholyte',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_15b852b5_19cc_49ab_849f_7df6175fb2be',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Catholyte',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    