
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AmountConcentrationModule import AmountConcentration



from .ElectrochemicalThermodynamicQuantityModule import ElectrochemicalThermodynamicQuantity







class IonConcentration(AmountConcentration, ElectrochemicalThermodynamicQuantity):
    """
    Class representing the `IonConcentration` entity, which inherits from:
    - AmountConcentration, ElectrochemicalThermodynamicQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8177eae6_1631_430d_99f2_942669bcb784'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IonConcentration'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IonConcentration(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8177eae6_1631_430d_99f2_942669bcb784',
    
    class_name='IonConcentration',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8177eae6_1631_430d_99f2_942669bcb784',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IonConcentration',
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
    

    
    

    

    