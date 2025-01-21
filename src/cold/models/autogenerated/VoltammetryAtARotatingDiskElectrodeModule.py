
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HydrodynamicVoltammetryModule import HydrodynamicVoltammetry







class VoltammetryAtARotatingDiskElectrode(HydrodynamicVoltammetry):
    """
    Class representing the `VoltammetryAtARotatingDiskElectrode` entity, which inherits from:
    - HydrodynamicVoltammetry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#VoltammetryAtARotatingDiskElectrode'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VoltammetryAtARotatingDiskElectrode'`
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
    obj = VoltammetryAtARotatingDiskElectrode(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#VoltammetryAtARotatingDiskElectrode',
    
    class_name='VoltammetryAtARotatingDiskElectrode',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#VoltammetryAtARotatingDiskElectrode',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VoltammetryAtARotatingDiskElectrode',
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
    

    
    

    

    