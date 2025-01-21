
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatioQuantityModule import RatioQuantity



from .ElectrochemicalKineticQuantityModule import ElectrochemicalKineticQuantity







class ChargeTransferCoefficient(RatioQuantity, ElectrochemicalKineticQuantity):
    """
    Class representing the `ChargeTransferCoefficient` entity, which inherits from:
    - RatioQuantity, ElectrochemicalKineticQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a4dfa5c1_55a9_4285_b71d_90cf6613ca31'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargeTransferCoefficient'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargeTransferCoefficient(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a4dfa5c1_55a9_4285_b71d_90cf6613ca31',
    
    class_name='ChargeTransferCoefficient',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a4dfa5c1_55a9_4285_b71d_90cf6613ca31',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargeTransferCoefficient',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    