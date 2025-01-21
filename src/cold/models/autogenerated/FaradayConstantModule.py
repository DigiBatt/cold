
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIExactConstantModule import SIExactConstant



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class FaradayConstant(SIExactConstant, ElectrochemicalQuantity):
    """
    Class representing the `FaradayConstant` entity, which inherits from:
    - SIExactConstant, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_77f9d496_555e_4ae2_ae80_f297ef8335ca'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FaradayConstant'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FaradayConstant(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_77f9d496_555e_4ae2_ae80_f297ef8335ca',
    
    class_name='FaradayConstant',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_77f9d496_555e_4ae2_ae80_f297ef8335ca',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FaradayConstant',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    