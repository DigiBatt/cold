
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MassConcentrationModule import MassConcentration



from .ThermodynamicalQuantityModule import ThermodynamicalQuantity







class MassConcentrationOfWaterVapour(MassConcentration, ThermodynamicalQuantity):
    """
    Class representing the `MassConcentrationOfWaterVapour` entity, which inherits from:
    - MassConcentration, ThermodynamicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_df8b283c_c02a_4158_b65e_60de7bb0b550'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassConcentrationOfWaterVapour'`
        - **Alias**: `class_name`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MassConcentrationOfWaterVapour(
    
    class_iri='https://w3id.org/emmo#EMMO_df8b283c_c02a_4158_b65e_60de7bb0b550',
    
    class_name='MassConcentrationOfWaterVapour',
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_df8b283c_c02a_4158_b65e_60de7bb0b550',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassConcentrationOfWaterVapour',
        alias="class_name"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    