
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPropertyModule import ElectrochemicalProperty







class ChargeRetention(ElectrochemicalProperty):
    """
    Class representing the `ChargeRetention` entity, which inherits from:
    - ElectrochemicalProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_49efb72a_f8e6_4f50_acac_975302200d47'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargeRetention'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargeRetention(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_49efb72a_f8e6_4f50_acac_975302200d47',
    
    class_name='ChargeRetention',
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_49efb72a_f8e6_4f50_acac_975302200d47',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargeRetention',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    