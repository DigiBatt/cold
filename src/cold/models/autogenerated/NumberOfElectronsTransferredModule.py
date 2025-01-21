
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PureNumberQuantityModule import PureNumberQuantity



from .ElectrochemicalKineticQuantityModule import ElectrochemicalKineticQuantity







class NumberOfElectronsTransferred(PureNumberQuantity, ElectrochemicalKineticQuantity):
    """
    Class representing the `NumberOfElectronsTransferred` entity, which inherits from:
    - PureNumberQuantity, ElectrochemicalKineticQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_abfadc99_6e43_4d37_9b04_7fc5b0f327ae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfElectronsTransferred'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumberOfElectronsTransferred(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_abfadc99_6e43_4d37_9b04_7fc5b0f327ae',
    
    class_name='NumberOfElectronsTransferred',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_abfadc99_6e43_4d37_9b04_7fc5b0f327ae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfElectronsTransferred',
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
    

    
    

    

    